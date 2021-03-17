<template>
    <tr>
        <td class="values-list">
            <span class="values-name"
                v-if="!editingMode"
            >{{valuesName}}</span>
            <form v-else @submit.prevent="endEdit()">
             <input @blur="startEdit()" v-model="newValuesString" type="text" />
            </form>
        </td>
        <td class="btn-container">
            <button @click="startEdit()" class="btn-edit">Edit</button>
            <button v-if="!editingMode" @click="$emit('on-delete_val')" class="btn-delete">Delete</button>
        </td>
    
    </tr>
</template>

<script>
export default {
    props: {
        valuesName: String
    },
    data() {
        return {
            editingMode: false,
            newValuesString: ""
        }
    },
    methods: {
    // Enter editing mode.
        startEdit() {
            if (!this.editingMode) {
                this.newValuesString = this.valuesName
                this.editingMode = true
            } else {
                this.endEdit();
            }
        },
    // Exit editing mode.
        endEdit() {
            this.editingMode = false;
            this.$emit('on-edit_val', this.newValuesString)
        }
    },
}
</script>

<style>

</style>