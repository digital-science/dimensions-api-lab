document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('a[href^="http://"], a[href^="https://"]').forEach((anchor) => {
    if (anchor.classList.contains("internal")) {
      return;
    }
    const href = anchor.getAttribute("href") || "";
    try {
      const url = new URL(href, window.location.origin);
      if (url.origin === window.location.origin) {
        return;
      }
    } catch {
      return;
    }
    anchor.setAttribute("target", "_blank");
    anchor.setAttribute("rel", "noopener noreferrer");
  });
});
