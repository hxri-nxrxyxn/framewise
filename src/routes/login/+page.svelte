<script>
  import { handleBackButton } from "../../script";

  handleBackButton("/");

  let username = $state("");
  let password = $state("");
  const onclick = () => {
    alert("button pressed");
  };
</script>

<main>
  <h1>login</h1>
  <input type="text" bind:value={username} />
  <input type="password" bind:value={password} />
  <button {onclick}>login</button>
  <a href="/">home</a>
  <a href="/signup">signup</a>
</main>

<style>
</style>
