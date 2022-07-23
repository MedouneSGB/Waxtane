<script>
  const storedWord = localStorage.getItem("word");
  let word = storedWord || "?";
</script>
<header>
    <h1><span class="text-gradient">Waxtane</span> Add word "{word}"</h1>
    <p class="instructions"><strong>Niewlene niou waxtane</strong> , venez discuter, come discuss with us !</p>
</header>
<main>
  <div class="link-card">
    <form name="contact" method="POST" data-netlify="true">
      <p>
        <label>Anglais <input type="text" name="anglais" value={word} required /></label>
      </p>
      <p>
        <label>Français <input type="text" name="français" value={word} required /></label>
      </p>
      <p>
        <label>Wolof <input type="text" name="Wolof" value={word} required /></label>
      </p>
      <p>
        <button type="submit">Envoyer</button>
      </p>
    </form>
  </div>
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

	.link-card > a, .link-card > form {
		width: 100%;
		text-decoration: none;
		line-height: 1.4;
		padding: 1em 1.3em;
		border-radius: 0.35rem;
		color: var(--text-color);
		background-color: white;
		opacity: 0.8;
	}

	h2 {
		margin: 0;
		transition: color 0.6s cubic-bezier(0.22, 1, 0.36, 1);
	}
    
  p {
      margin-top: 0.75rem;
      margin-bottom: 0;
  }

	h2 span {
		display: inline-block;
		transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1);
	}

	.link-card:is(:hover, :focus-within) {
		background-position: 0;
	}

	.link-card:is(:hover, :focus-within) h2 {
		color: #4F39FA;
	}

	.link-card:is(:hover, :focus-within) h2 span {
		transform: translateX(2px);
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