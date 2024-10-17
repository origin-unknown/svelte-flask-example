export const prerender = true;
export const ssr = false;

/** @type {import('./$types').PageLoad} */
export async function load({ params, fetch }) {
	const users = await fetch('/data')
		.then(resp => resp.ok && resp.json());
	return { users };
}