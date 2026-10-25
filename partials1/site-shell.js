/* Site-wide shell: shared navigation, footer and a single tracker activation. */
(function () {
  "use strict";
  if (window.__smSiteShellInitialized) return;
  window.__smSiteShellInitialized = true;

  const HEADER = "/partials1/header.html";
  const FOOTER = "/partials1/footer.html";

  function getOrCreate(id, first) {
    let node = document.getElementById(id);
    if (node) return node;
    node = document.createElement("div");
    node.id = id;
    if (first) {
      const skip = document.body.querySelector(":scope > a.skip, :scope > a.skip-link");
      if (skip) skip.insertAdjacentElement("afterend", node);
      else document.body.prepend(node);
    } else document.body.append(node);
    return node;
  }

  function activateTracker(headerRoot) {
    const embedded = headerRoot.querySelector("script[data-metricool-tracker]");
    if (!embedded || window.__smMetricoolTrackingStarted) return;
    window.__smMetricoolTrackingStarted = true;
    // Script tags inserted with innerHTML do not run. Re-insert this one explicitly.
    const live = document.createElement("script");
    live.textContent = embedded.textContent;
    embedded.replaceWith(live);
  }

  async function loadPartial(node, url, isHeader) {
    try {
      const response = await fetch(url, { cache: "no-cache" });
      if (!response.ok) throw new Error("HTTP " + response.status);
      node.innerHTML = await response.text();
      if (isHeader) activateTracker(node);
    } catch (error) {
      console.warn("Kunde inte ladda gemensam layout: " + url, error);
    }
  }

  function init() {
    const header = getOrCreate("site-header", true);
    const footer = getOrCreate("site-footer", false);
    void loadPartial(header, HEADER, true);
    void loadPartial(footer, FOOTER, false);
  }

  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
