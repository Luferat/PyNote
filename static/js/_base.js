if (window.history.replaceState) window.history.replaceState(null, null, window.location.href);

$(document).ready(mainApp)

function mainApp() {
    runResize()
    $('#menuToggle').click(menuToggle)
    $(window).resize(runResize)
    $('#courtain').click(runResize)
    $('#toggleExpand').click(expandToggle)
}

function menuToggle() {
    if ($('#mainNav').is(':visible')) hideMenu()
    else showMenu()
    return false
}

function hideMenu() {
    $('#mainNav').hide('fast', () => {
        $('#courtain').hide('fast', () => {
            $('#menuToggle').html('<i class="fa-solid fa-bars fa-fw"></i>')
        })
    })
}

function showMenu(courtain = true) {
    if (courtain) $('#courtain').show('fast')
    else $('#courtain').hide()
    $('#mainNav').show('fast', () => {
        $('#menuToggle').html('<i class="fa-solid fa-xmark fa-fw"></i>')
    })
}

function runResize() {
    if (window.innerWidth < 575) {
        hideMenu()
        $('#menuToggle').show()
    } else {
        showMenu(false)
        $('#menuToggle').hide()
    }
}

function expandToggle() {
    if ($('#cssVars').attr('href') == '/static/css/vars_wrap.css') {
        $('#cssVars').attr('href', '/static/css/vars_full.css')
        $('#toggleExpand').html('<i class="fa-solid fa-compress fa-fw"></i><span>Comprimir</span>')
    } else {
        $('#cssVars').attr('href', '/static/css/vars_wrap.css')
        $('#toggleExpand').html('<i class="fa-solid fa-expand fa-fw"></i><span>Expand</span>')
    }
    return false
}