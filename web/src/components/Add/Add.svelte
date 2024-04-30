<script>
  const storedWord = localStorage.getItem("word");
  let word = storedWord || "?";
  let wordShowed = word;
	
  if (word == '?' || null || undefined){
	  word = "";
	  wordShowed = "?";
  }

  let submit = false
  let send = false
	
	const handleSubmit = e => {
		submit = true

		const formData = new FormData(e.target)
		const data = new URLSearchParams()
		for (let field of formData) {
			const [key, value] = field
			data.append(key, value)
		}

    fetch("/", {
      method: 'POST',
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: data
    })
    .then(() => send = true)
    .catch((error) => alert(error));

	}
	
	const handleKeyup = () => {
		submit = false
		
		if (event.code == 'Enter') {
			event.preventDefault()
			event.target.value
			value = event.target.value
			return false
		}
	}
</script>
<header>
    <h1><span class="text-gradient">Waxtane</span> Add word "{wordShowed}"</h1>
    {#if send}
      <p class="instructions vert">
        <strong>Merci !</strong> Votre contributin à été bien enregistrées.
      </p>
    {:else}
      <p class="instructions gradient"><strong>Niewlene niou waxtane</strong> , venez discuter, come discuss with us !</p>
    {/if}
</header>
<main>
  {#if send}
    <p>Après verification il sera ajouté a la liste</p>
  {:else}
  <div class="link-card">
    <form name="waxtane" method="POST" data-netlify="true" on:submit|preventDefault={handleSubmit}>
      <input type="hidden" name="form-name" value="waxtane">
      <p>
        <label>Anglais <input type="text" name="anglais" value={word} required on:keyup|preventDefault={handleKeyup}/></label>
      </p>
      <p>
        <label>Français <input type="text" name="francais" value={word} required on:keyup|preventDefault={handleKeyup}/></label>
      </p>
      <p>
        <label>Wolof <input type="text" name="wolof" value={word} required on:keyup|preventDefault={handleKeyup}/></label>
      </p>
      <p>
        <button type="submit">Envoyer</button>
      </p>
    </form>
  </div>
  {/if}
</main>
<style>
	.link-card {
		list-style: none;
		display: flex;
		padding: 0.15rem;
		background-image: var(--link-gradient);
		background-size: 400%;
		border-radius: 0.5rem;
		background-position: 100%;
		transition: background-position 0.6s cubic-bezier(0.22, 1, 0.36, 1);
	}
  
	.link-card > form {
		width: 100%;
		text-decoration: none;
		line-height: 1.4;
		padding: 1em 1.3em;
		border-radius: 0.35rem;
		color: var(--text-color);
		background-color: white;
		opacity: 0.8;
	}
    
  p {
      margin-top: 0.75rem;
      margin-bottom: 0;
  }

	.link-card:is(:hover, :focus-within) {
		background-position: 0;
	}

  label, input, button {
    display: block;
    width: 100%;
    padding: 0;
    border: none;
    outline: none;
    box-sizing: border-box;
  }

  label {
    margin-bottom: 4px;
  }

  label:nth-of-type(2) {
    margin-top: 12px;
  }

  input::placeholder {
    color: gray;
  }

  input {
    background: #ecf0f3;
    padding: 10px;
    padding-left: 20px;
    height: 50px;
    font-size: 14px;
    border-radius: 50px;
    box-shadow: inset 6px 6px 6px #cbced1, inset -6px -6px 6px white;
  }


	button {
    color: white;
    margin-top: 20px;
    background: #4F39FA;
    height: 40px;
    border-radius: 20px;
    border-color: transparent;
    cursor: pointer;
    font-weight: 900;
    box-shadow: 6px 6px 6px #cbced1, -6px -6px 6px white;
    transition: 0.5s;
  }

  button:hover {
    box-shadow: none;
  }
</style>
