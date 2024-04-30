<script>
  import AutoComplete from "simple-svelte-autocomplete"

  export let data

  const customize = {
    "searchPlaceholders":{
		  "Anglais": "Search a word",
		  "Français": "Cherche un mot",
		  "Wolof": "Saytu ben baat"
	  },
    "noResultsText":{
		  "Anglais": "No results found",
		  "Français": "Aucun résultat trouvé",
		  "Wolof": "Giso sa laaj"
	  },
    "addWord":{
      "Anglais": "Propose this word",
		  "Français": "Proposez ce mot",
		  "Wolof": "Yokkal baat bi"
    }
  }
	
  let selectedwaxtane = null
  let text = ''
  let lang = "Wolof"

  const forceUpdate = async (_) => {};

  function toggle(event) {
		lang = event.target.innerHTML;
	}

</script>

<h1>Search in {lang}</h1>

<div class="lang">
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
  <AutoComplete items="{data}" bind:selectedItem="{selectedwaxtane}" bind:text bind:labelFieldName={lang} placeholder="{customize.searchPlaceholders[lang]}" className="search" inputClassName="search-input">
    <div slot="no-results">
       <strong>{customize.noResultsText[lang]} <a href={`/add?word=${text}`}>{customize.addWord[lang]}</a></strong>
    </div>
  </AutoComplete>
  {#if selectedwaxtane}
    <table>
      <tr>
        <th>N°</th>
        <th>Wolof</th>
        <th>Français</th>
        <th>Anglais</th>
        <th>Espagnol</th>
      </tr>
      <tr>
        <td>{selectedwaxtane.1}</td>
        <td>{selectedwaxtane.Wolof}</td>
        <td>{selectedwaxtane.Français}</td>
        <td>{selectedwaxtane.Anglais}</td>
        <td>{selectedwaxtane.Espagnol}</td>
      </tr>
    </table>
  {/if}
{/await}
