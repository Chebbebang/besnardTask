<template>
    <tr>
        <td class="principles-list">
            <span class="principles-name"
                v-if="!editingMode"
            >{{principlesName}}</span>
            <form v-else @submit.prevent="endEdit()">
                <input @blur="startEdit()" v-model="newPrincipleString" type="text" />
            </form>
        </td>
        <td>
            <button @click="startEdit()" class="btn-edit">Edit</button>
            <button v-if="!editingMode" @click="$emit('on-delete_pri')" class="btn-delete">Delete</button>
        </td>
    </tr>
</template>

<script>
export default {
    props: {
        principlesName: String
    },
    data() {
        return {
            editingMode: false,
            newPrincipleString: ""
        }
    },
    methods: {
    // Enter editing mode.
        startEdit() {
            if (!this.editingMode) {
                this.newPrincipleString = this.principlesName
                this.editingMode = true
            } else {
                this.endEdit();
            }
        },
    // Exit editing mode.
        endEdit() {
            this.editingMode = false;
            this.$emit('on-edit_pri', this.newPrincipleString)
        }
    },
}
</script>

<style>

</style>