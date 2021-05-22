<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';

  let loading = true;
  let item = null;

  onMount(async () => {
    let m = window.location.pathname.match(/^\/airplane\/(\d+)$/);
    const res = await fetch(`http://localhost:3001/detail/${m[1]}`);
    item = await res.json();
    loading = false
  });

</script>

<svelte:head>
  <title>Airplane Detail</title>
</svelte:head>

<div class="content">
  <h1>Airplanes</h1>
  {#if loading}
    <p>Loading...</p>
  {:else}
    <h3>
      <a href="/airplanes">Airplanes</a> &gt; {item.manufacturer} {item.name}
    </h3>
    <a href={item.wiki}>
      <img src={item.image}>
    </a>
  {/if}
</div>

<style>
  .content {
    width: 100%;
    max-width: var(--column-width);
    margin: var(--column-margin-top) auto 0 auto;
  }
</style>
