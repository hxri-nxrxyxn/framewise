<script>
  import { handleBackButton, signup } from "../../script";

  handleBackButton("/");

  let email = $state("");
  let password = $state("");
  const onclick = () => {
    const data = { email, password };
    signup(data);
  };
</script>

<main>
  <h1>signup</h1>
  <input type="text" bind:value={email} />
  <input type="password" bind:value={password} />
  <button {onclick}>signup</button>
  <a href="/">home</a>
  <a href="/login">login</a>
</main>

<style>
</style>
