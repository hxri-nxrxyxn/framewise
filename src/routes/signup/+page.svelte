<script>
    import { handleBackButton, signup } from "../../script";
    import Nav from "$lib/Nav.svelte";
    handleBackButton("/");

    let email = $state("");
    let password = $state("");
    let name = $state("");
    const onclick = () => {
        const data = { email, password, name };
        signup(data);
    };
</script>

<Nav message="READY FOR" bold="AUTH" />
<main>
    <h1 class="head">SIGN UP</h1>
    <img src="/welcome.svg" alt="" class="cover" />
    <div class="form">
        <div class="form__line">
            <label>NAME</label>
            <input type="text" placeholder="Hari Narayan" bind:value={name} />
        </div>
        <div class="form__line">
            <label>EMAIL</label>
            <input
                type="email"
                placeholder="hari@laddu.cc"
                bind:value={email}
            />
        </div>
        <div class="form__line">
            <label>PASSWORD</label>
            <input type="password" bind:value={password} />
        </div>
    </div>

    <div class="buttons">
        <!-- svelte-ignore a11y_click_events_have_key_events -->
        <div class="button" {onclick}>CONTINUE</div>
    </div>
</main>

<style>
    .buttons {
        width: calc(100vw - 4rem);
        margin: 3rem 0;
        justify-content: center;
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
