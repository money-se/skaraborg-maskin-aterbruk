-- Skaraborg Maskin & Återbruk / Annonsadmin
-- Apply only to a Supabase PROJECT YOU CONTROL after review.
-- Before running: create a public Storage bucket named ad-images in the dashboard.
begin;
create extension if not exists pgcrypto;
create table if not exists public.ad_editors (
  user_id uuid primary key references auth.users(id) on delete cascade,
  created_at timestamptz not null default now()
);
create table if not exists public.ads (
  id uuid primary key default gen_random_uuid(),
  title text not null check (length(btrim(title)) between 1 and 120),
  description text not null default '' check (length(description) <= 2500),
  price_sek integer not null check (price_sek between 0 and 10000000),
  status text not null default 'sale' check (status in ('sale','pending','sold')),
  published boolean not null default true,
  image_paths text[] not null default '{}',
  created_by uuid not null default auth.uid() references auth.users(id),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint max_images check (cardinality(image_paths) <= 6)
);
create index if not exists ads_public_idx on public.ads(status, created_at desc) where published;
alter table public.ad_editors enable row level security;
alter table public.ads enable row level security;
revoke all on public.ad_editors from anon, authenticated;
grant select on public.ad_editors to authenticated;
grant select on public.ads to anon, authenticated;
grant insert,update,delete on public.ads to authenticated;
drop policy if exists "Editors see own membership" on public.ad_editors;
create policy "Editors see own membership" on public.ad_editors for select to authenticated using (user_id=(select auth.uid()));
create or replace function public.is_ad_editor()
returns boolean language sql stable security definer set search_path=''
as $$ select exists (select 1 from public.ad_editors where user_id=(select auth.uid())); $$;
revoke all on function public.is_ad_editor() from public, anon;
grant execute on function public.is_ad_editor() to authenticated;
drop policy if exists "Visitors see active published ads" on public.ads;
create policy "Visitors see active published ads" on public.ads
for select to anon using (published and status in ('sale','pending'));
drop policy if exists "Editors see all ads" on public.ads;
create policy "Editors see all ads" on public.ads
for select to authenticated using (public.is_ad_editor());
drop policy if exists "Editors insert ads" on public.ads;
create policy "Editors insert ads" on public.ads
for insert to authenticated with check (public.is_ad_editor() and created_by=(select auth.uid()));
drop policy if exists "Editors update ads" on public.ads;
create policy "Editors update ads" on public.ads
for update to authenticated using (public.is_ad_editor()) with check (public.is_ad_editor());
drop policy if exists "Editors delete ads" on public.ads;
create policy "Editors delete ads" on public.ads
for delete to authenticated using (public.is_ad_editor());
create or replace function public.ads_set_updated_at() returns trigger language plpgsql set search_path='' as $$
begin
  new.updated_at = now();
  if tg_op='UPDATE' then new.created_by=old.created_by; end if;
  return new;
end $$;
drop trigger if exists ads_updated_at on public.ads;
create trigger ads_updated_at before update on public.ads for each row execute function public.ads_set_updated_at();
-- Public bucket ad-images MUST exist before creating these policies.
drop policy if exists "Anyone reads ad images" on storage.objects;
create policy "Anyone reads ad images" on storage.objects
for select to anon,authenticated using (bucket_id='ad-images');
drop policy if exists "Editors upload ad images" on storage.objects;
create policy "Editors upload ad images" on storage.objects
for insert to authenticated with check (bucket_id='ad-images' and public.is_ad_editor());
drop policy if exists "Editors remove ad images" on storage.objects;
create policy "Editors remove ad images" on storage.objects
for delete to authenticated using (bucket_id='ad-images' and public.is_ad_editor());
commit;
-- Add ONLY the intended auth.users IDs manually through SQL Editor,
-- e.g. insert into public.ad_editors(user_id) values ('YOUR-USER-UUID');
-- NEVER include service_role credentials in GitHub or browser JavaScript.
