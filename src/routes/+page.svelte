<script lang="ts">
	import Pixel from '$lib/components/Pixel.svelte';
	import Result from '$lib/components/Result.svelte';
	import { loadModel } from '$lib/functions/callModel';
  import { div, tensor } from '@tensorflow/tfjs';

  let matrix = $state(Array.from({ length: 28 }, () => Array(28).fill(false)));

  function clearMatrix(){
    matrix = Array.from({ length: 28 }, () => Array(28).fill(false))

  }

  let prediction = $state(0)
  let confidence = $state(0)

  async function identifyDigit(){
    let response = await fetch("http://localhost:8080/", {
      method: "POST", 
      headers: {
        "Content-Type": "application/json", 
      },
      body: JSON.stringify(matrix)
    }) 

    let data = await response.json()
    prediction = data["prediction"]
    confidence = data["confidence"]

  }

</script>

<Result { prediction } {confidence}></Result>
<button onclick={() => identifyDigit()} class="bg-black text-white rounded-lg p-3">Identify</button>
<button onclick={() => clearMatrix()} class="bg-red-300 text-white rounded-lg p-3">Clear</button>
<div class="w-full p-8 grid place-items-center">
	{#each Array(28) as _, indexI}
		<div class="flex flex-row">
			{#each Array(28) as _, indexJ}
				<Pixel bind:colored={matrix[indexI][indexJ]}></Pixel>
			{/each}
		</div>
	{/each}
</div>
