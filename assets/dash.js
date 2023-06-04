window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        executar_codigo: function(n_clicks) {
            if (n_clicks) {
                document.body.style.backgroundColor = "#f00";
                document.body.style.color = "#ff0";
                return 'O botão foi clicado!';
            }
        }
    }
});
