# React + Babel Setup for Inline JSX

> **Load when:** Building React prototypes with inline JSX
> **Skip when:** Working with plain HTML/CSS only
> **Why it matters:** Pinned versions and integrity hashes prevent runtime breakage; scope rules prevent global variable collisions between component files
> **Typical failure it prevents:** React version mismatch, `styles` object overwrites across components, Babel scope isolation breaking component sharing

Use these exact script tags with pinned versions and integrity hashes when writing React prototypes with inline JSX. Do not use unpinned versions (e.g. react@18) or omit the integrity attributes.

```html
<script src="https://unpkg.com/react@18.3.1/umd/react.development.js" integrity="sha384-hD6/rw4ppMLGNu3tX5cjIb+uRZ7UkRJ6BPkLpg4hAu/6onKUg4lLsHAs9EBPT82L" crossorigin="anonymous"></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js" integrity="sha384-u6aeetuaXnQ38mYT8rp6sbXaQe3NL9t+IBXmnYxwkUI2Hw4bsp2Wvmx4yRQF1uAm" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" integrity="sha384-m08KidiNqLdpJqLq95G/LEi8Qvjl/xUYll3QILypMoQ65QorJ9Lvtp2RXYGBFj1y" crossorigin="anonymous"></script>
```

Import helper or component scripts using script tags. Avoid using `type="module"` on script imports — it may break things.

## Scope Rules

**CRITICAL: When defining global-scoped style objects, give them SPECIFIC names.** If you import >1 component with a `styles` object, it will break. Each must have a unique name based on the component:

```js
const terminalStyles = { ... };  // NOT const styles = { ... }
```

**CRITICAL: Multiple Babel script files don't share scope.** Each `<script type="text/babel">` gets its own scope when transpiled. Export components to `window` at the end of each component file:

```js
// At the end of components.jsx:
Object.assign(window, {
  Terminal, Line, Spacer,
  Gray, Blue, Green, Bold,
  // ... all components that need to be shared
});
```
