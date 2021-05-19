<script>
  import { onMount } from 'svelte';

  let loading = true;
  let items = null;

  onMount(async () => {
    const res = await fetch(`http://localhost:3001/list`);
    items = await res.json();
    loading = false
  });

</script>

<svelte:head>
  <title>Airplanes</title>
</svelte:head>

<div class="content">
  <h1>Airplanes</h1>
  {#if loading}
    <p>Loading...</p>
  {:else}
    {#each items as item}
      <div>
        <h3>
          <a href={`/airplane/${item.id}`}>{item.manufacturer} {item.name}</a>
        </h3>
      </div>
    {/each}
  {/if}
</div>

<style>
  .content {
    width: 100%;
    max-width: var(--column-width);
    margin: var(--column-margin-top) auto 0 auto;
  }
</style>
