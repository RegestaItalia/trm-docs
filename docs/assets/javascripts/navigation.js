const expandedSidebarGroups = new Set(["Getting Started", "Examples"]);
const desktopSidebar = window.matchMedia("(min-width: 76.25em)");

function keepSelectedSidebarGroupsExpanded() {
  const topLevelItems = document.querySelectorAll(
    ".md-nav--primary > .md-nav__list > .md-nav__item--nested"
  );

  for (const item of topLevelItems) {
    const title = item.querySelector(":scope > .md-nav__link .md-ellipsis");
    const toggle = item.querySelector(":scope > .md-nav__toggle");

    if (title && toggle && expandedSidebarGroups.has(title.textContent.trim())) {
      if (toggle.dataset.initiallyChecked === undefined) {
        toggle.dataset.initiallyChecked = String(toggle.checked);
      }

      if (desktopSidebar.matches) {
        toggle.checked = true;
        toggle.disabled = true;
        item.dataset.alwaysExpanded = "true";
      } else {
        toggle.checked = toggle.dataset.initiallyChecked === "true";
        toggle.disabled = false;
        delete item.dataset.alwaysExpanded;
      }
    }
  }
}

keepSelectedSidebarGroupsExpanded();
desktopSidebar.addEventListener("change", keepSelectedSidebarGroupsExpanded);

if (typeof document$ !== "undefined") {
  document$.subscribe(keepSelectedSidebarGroupsExpanded);
}

// The contributors page reports its height as its grid reflows; the iframe
// cannot be measured cross-origin.
window.addEventListener("message", (event) => {
  if (event.origin !== "https://trmregistry.com" || event.data?.type !== "trm-contributors:height") return;
  for (const frame of document.querySelectorAll(".contributors-embed__iframe")) {
    if (frame.contentWindow === event.source) frame.style.height = `${event.data.height}px`;
  }
});
