<script>
  import AutoComplete from "simple-svelte-autocomplete"

  export let data
  
  let selectedwaxtane = null
  let lang = "Wolof"

  const forceUpdate = async (_) => {};

  function toggle(event) {
		lang = event.target.innerHTML;
	}

</script>

<h1>Search in {lang}</h1>

<div>
  <button on:click={toggle}>
	  Wolof
  </button>
  <button on:click={toggle}>
    Français
  </button>
  <button on:click={toggle}>
    Anglais
  </button>
</div>

<style>
  table {
    width: 100%;
  }
</style>

{#await forceUpdate(lang) then _}
  <AutoComplete items="{data}" bind:selectedItem="{selectedwaxtane}" bind:labelFieldName={lang} placeholder="Search a word" className="search" />
  {#if selectedwaxtane}
    <table>
      <tr>
        <th>N°</th>
        <th>Wolof</th>
        <th>Français</th>
        <th>Anglais</th>
      </tr>
      <tr>
        <td>{selectedwaxtane['N°']}</td>
        <td>{selectedwaxtane.Wolof}</td>
        <td>{selectedwaxtane.Français}</td>
        <td>{selectedwaxtane.Anglais}</td>
      </tr>
    </table>
  {/if}
{/await}
