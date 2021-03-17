<template>
    <div>
        <form @submit.prevent="addPrinciple()">
            <input v-model="newPrinciple" placeholder="Enter new Value" type="text" class="new-input">
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            newPrinciple: ""
        }
    },
    methods: {
        addPrinciple() {
            if (this.newPrinciple.length > 1) {
                this.$emit("on-new_Principle", this.newPrinciple);
            }
            this.newPrinciple = "";
        }
    },
}
</script>

<style>
    
</style>