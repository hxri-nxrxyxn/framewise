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

<nav>
    <p>FRAMEWISE</p>
    <img src="/lock.svg" alt="hey" />
</nav>
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
        <div class="button" {onclick}>LOGIN</div>
        <div class="button" {onclick}>SIGNUP</div>
    </div>
</main>

<style>
    .buttons {
        width: calc(100vw - 4rem);
        margin: 2rem 0;
        margin-top: 3rem;
    }
    .button {
        width: 50%;
    }
    .button:last-child {
        margin-left: 1rem;
    }
    .button:first-child {
        background: var(--color-primary);
        color: white;
    }
</style>
