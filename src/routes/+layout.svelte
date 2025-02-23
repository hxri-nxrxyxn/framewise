<script>
    import "../app.css";
    import { slide } from "svelte/transition";
    import { page } from "$app/stores";
    import { quintOut } from "svelte/easing";
</script>

{#key $page.url.pathname}
    <div>
        <slot />
    </div>
{/key}
