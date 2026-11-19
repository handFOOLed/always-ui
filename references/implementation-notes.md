# Implementation notes (read only for relevant tasks)

These patterns are examples, not framework mandates. Adapt to the actual UI framework and supported browsers/hosts.

## Focus ring with high-contrast fallback

For a custom visible keyboard focus indicator, preserve an outline as the robust layer and optionally add a visual halo. The browser's native default is often sufficient.

```css
.control:focus-visible {
  outline: 2px solid var(--focus-color, currentColor);
  outline-offset: 2px;
  box-shadow: 0 0 0 4px var(--focus-halo, transparent);
}

@media (forced-colors: active) {
  .control:focus-visible {
    outline: 2px solid Highlight;
    box-shadow: none;
  }
}
```

Test the result against adjacent colors, zoom, clipping, and selected states. Do not treat a soft shadow as the sole focus indicator.

## Expandable regions

`grid-template-rows: 0fr` → `1fr` can be a useful content-sized transition **when the surrounding structure supports it**. The inner wrapper must be min-size aware and clipped; the collapsed content must be inert/hidden from keyboard and assistive technology as appropriate. If that cannot be achieved reliably, use a native disclosure, supported discrete transition, or instant expand/collapse instead.

```css
.expandable {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 180ms ease;
}
.expandable[data-open="true"] { grid-template-rows: 1fr; }
.expandable > .inner { min-height: 0; overflow: hidden; }
@media (prefers-reduced-motion: reduce) {
  .expandable { transition: none; }
}
```

**Important:** This snippet handles visual height only. It does not implement `aria-expanded`, focus movement, keyboard deactivation, inertness, or semantic disclosure. The framework must manage those explicitly. Test long text, dynamic loading, fast reversal, and focus while closing.

## Filename display

Keep the original path/name in application state. Render a visually shortened **display label**, not a renamed file. A common pattern is separately laid-out flexible basename and nonshrinking extension. Define extension rules for extensionless names, leading-dot filenames (such as `.gitignore`), compound extensions (`.tar.gz`), trailing dots, and right-to-left text according to the product's file semantics. Keep the full name accessible via copy, detail view, and/or accessible label. Do not rely on `text-overflow: ellipsis` on the whole filename when extension recognition matters.

## Stable numbers

```css
.counter, .timestamp, .numeric-column {
  font-variant-numeric: tabular-nums;
}
```

Check that the selected font supports tabular numerals; otherwise use a font fallback or another alignment strategy.

## Native desktop window dragging

Use the window host's documented drag-region API (e.g., the appropriate Tauri, Electron, or platform-native mechanism). Define the drag region on noninteractive sidebar/titlebar surfaces only, explicitly exclude interactive descendants according to host rules, and verify dragging, double-click behavior, text selection, window controls, and resize. Browser-only pages have no application-window drag requirement.
