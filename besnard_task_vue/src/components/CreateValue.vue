<template>
    <div>
        <form @submit.prevent="addValue()">
            <input v-model="newValue" placeholder="Enter new Value" type="text" class="new-input">
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            newValue: ""
        }
    },
    methods: {
        addValue() {
            if (this.newValue.length > 1) {
                this.$emit("on-new_Value", this.newValue);
            }
            this.newValue = "";
        }
    },
}
</script>

<style>
    
</style>