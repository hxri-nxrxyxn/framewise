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

<Nav message="LOGIN" bold="SECURELY" />
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
            <div class="button">
                SIGNUP
                <span>CUSTOM</span>
            </div>
        </a>
    </div>
</main>

<style>
    .button span {
        position: absolute;
        right: -0.75rem;
        top: -0.5rem;
        background: var(--color-secondary);
        padding: 0.15rem 1rem;
        font-weight: 600;
        font-size: 0.75rem;
        border: 1px solid var(--color-border);
        color: var(--color-grey);
    }
</style>
