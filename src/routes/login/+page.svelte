<script>
    import { handleBackButton, login } from "../../script";
    import Nav from "$lib/Nav.svelte";
    let email = $state("");
    let password = $state("");

    handleBackButton("/");

    const onclick = () => {
        const data = { email, password };
        login(data);
    };
</script>

<Nav />
<main>
    <h1 class="head">WELCOME</h1>
    <img src="/login.svg" alt="" class="cover" />
    <div class="form">
        <div class="form__line">
            <label>EMAIL</label>
            <input type="text" placeholder="hari@laddu.cc" bind:value={email} />
        </div>
        <div class="form__line">
            <label>PASSWORD</label>
            <input type="password" bind:value={password} />
        </div>
    </div>

    <div class="buttons">
        <div class="button button--orange" {onclick}>LOGIN</div>
        <a href="/signup">
            <div class="button">SIGNUP</div>
        </a>
    </div>
</main>

<style>
</style>
