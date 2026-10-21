const expandedSidebarGroups = new Set(["Getting Started", "Examples"]);

function keepSelectedSidebarGroupsExpanded() {
  const topLevelItems = document.querySelectorAll(
    ".md-nav--primary > .md-nav__list > .md-nav__item--nested"
  );

  for (const item of topLevelItems) {
    const title = item.querySelector(":scope > .md-nav__link .md-ellipsis");
    const toggle = item.querySelector(":scope > .md-nav__toggle");

    if (title && toggle && expandedSidebarGroups.has(title.textContent.trim())) {
      toggle.checked = true;
      toggle.disabled = true;
      item.dataset.alwaysExpanded = "true";
    }
  }
}

keepSelectedSidebarGroupsExpanded();

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
