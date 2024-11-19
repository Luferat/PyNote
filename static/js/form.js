$(document).ready(newApp)

function newApp() {

    $('#btnCategories').click(toggleCategories)
    $('#btnOk').click(toggleCategories)

}

function toggleCategories() {

    $('#catList>h4').html('Categorias de ' + $('#title').val())

    if (catList.open) {
        catList.close()
    } else {
        catList.showModal()
    }

}