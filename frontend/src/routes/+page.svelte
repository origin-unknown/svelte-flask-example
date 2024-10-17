<script>

/** @type {import('./$types').PageData} */
export let data;
const { users } = data;

</script>

<table>
	<tbody>
		{#each users as {id,name,desc}, i}
		<tr>
			<td>{ id }</td>
			<td>{ name }</td>
			<td>{ desc }</td>
		</tr>
		{/each}
	</tbody>
</table>