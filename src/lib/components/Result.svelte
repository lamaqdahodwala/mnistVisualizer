<script lang="ts">
	import { fade } from "svelte/transition";

  let {prediction, confidence} = $props()
</script>

<div class="border border-gray rounded-lg w-96 grid place-items-center m-3 p-3">
  <p transition:fade>Current prediction: {prediction}</p>
  <p transition:fade>Confidence: {confidence * 100}%</p>
</div>
