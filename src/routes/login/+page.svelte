<script>
  import { handleBackButton, login } from "../../script";
  
  let email = $state("");
  let password = $state("");
  
  handleBackButton("/");


  const onclick = () => {
    const data = { email, password };
    login(data);
  };

</script>

<main>
  <h1>login</h1>
  <input type="text" bind:value={email} />
  <input type="password" bind:value={password} />
  <button {onclick}>login</button>
  <a href="/">home</a>
  <a href="/signup">signup</a>
</main>

<style>
</style>
