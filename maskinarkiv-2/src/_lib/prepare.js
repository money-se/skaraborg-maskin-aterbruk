const fs = require("node:fs");
const path = require("node:path");
function rebase(markup) {
  return markup.replace(/(href|src)=(["'])([^"']+)\2/g, (whole, attr, quote, value) => {
    if (value.startsWith("/") || value.startsWith("#") || value.startsWith("?") || /^[a-z][a-z0-9+.-]*:/i.test(value)) return whole;
    return attr + "=" + quote + "/" + value.replace(/^\.\//,"") + quote;
  });
}
const root = path.resolve(__dirname,"../../../");
const header = rebase(fs.readFileSync(path.join(root,"partials1/header.html"),"utf8"));
const footer = rebase(fs.readFileSync(path.join(root,"partials1/footer.html"),"utf8"));
module.exports = function prepare(machine) {
  return {
    ...machine,
    headHtml: machine.headHtml.replace('<div id="site-header"></div>',header),
    footerHtml: machine.footerHtml
      .replace('<div id="site-footer"></div>',footer)
      .replace(/<script\b[^>]*>[\s\S]*?<\/script>/g, script => script.includes('inject(') ? '' : script),
  };
};
