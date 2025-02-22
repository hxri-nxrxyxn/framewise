<script>
    let username = $state("");
    let password = $state("");
    const onclick = () => {
        alert("button pressed");
    };
</script>

<main>
    <h1>signup</h1>
    <input type="text" bind:value={username} />
    <input type="password" bind:value={password} />
    <button {onclick}>signup</button>
    <a href="/">home</a>
    <a href="/login">login</a>
</main>

<style>
</style>
