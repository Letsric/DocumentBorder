import { c as create_ssr_component } from './index-1d92b199.js';

const css = {
  code: ".mainbox.svelte-193glp{width:60vw;margin-left:auto;margin-right:auto}.range.svelte-193glp{appearance:none;background:darkslategray;border-radius:1em;height:2em}.range.svelte-193glp::-webkit-slider-thumb{appearance:none;background-color:green;border:5px solid darkgreen;border-radius:0.5em;height:3em;width:3em}.range.svelte-193glp::-moz-range-thumb{background-color:green;border:5px solid darkgreen;border-radius:0.5em;height:3em;width:3em}.pos-abs.svelte-193glp{position:absolute}",
  map: null
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  $$result.css.add(css);
  return `<h1 class="${"title is-1"}">Document Border</h1>
<hr>

${`<div class="${"box mainbox svelte-193glp"}"><h2 class="${"title is-2 is-centered mb-6 mt-4"}">Bitte wähle zu beginn das Papierformat</h2>
		<div class="${"columns mb-4 mx-4"}"><div class="${"column"}"><button class="${"button is-outlined is-info is-fullwidth py-6 is-size-4"}">A3</button></div>
			<div class="${"column"}"><button class="${"button is-outlined is-info is-fullwidth py-6 is-size-4"}">A4</button></div>
			<div class="${"column"}"><button class="${"button is-outlined is-info is-fullwidth py-6 is-size-4"}">A5</button></div>
			<div class="${"column"}"><button class="${"button is-outlined is-info is-fullwidth py-6 is-size-4"}">US Letter</button></div></div></div>`}`;
});

export { Page as default };
//# sourceMappingURL=_page.svelte-e3dd24d8.js.map
