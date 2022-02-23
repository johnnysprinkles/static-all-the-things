<script context="module">
 export async function load({ url }) {
    try {
      return { props: { itemId : url.searchParams.get('id') } };
    } catch (e) {
      return { props: { itemId: '' } };
    }
  }
</script>
<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';

  export let itemId = null;
  let loading = true;
  let item = null;

  onMount(async () => {
    if(itemId){
      const res = await fetch(`http://localhost:3001/detail/${itemId}`);
      item = await res.json();
      loading = false
    }
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
