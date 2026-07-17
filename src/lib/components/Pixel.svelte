<script lang="ts">
	let { colored = $bindable(false) } = $props();

	function color(event: MouseEvent) {
		console.log(event);
		if (event.buttons === 1) {
			colored = true;
		}
	}

	function colorFromClick(event: PointerEvent) {
		colored = !colored;
	}
</script>

<div
	class="h-[28px] w-[28px] border border-black {colored ? 'bg-black' : ''}"
	onmouseover={(event) => color(event)}
	onmousedown={(event) => {
		colored = !colored;
	}}
></div>
