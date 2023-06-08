window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        iniciar_indexeddb: function() {
            const webappdb = window.indexedDB.open("WebAppDB", 1);

            webappdb.onupgradeneeded = function(event) {
                let db = event.target.result;
                db.createObjectStore("dados", { keyPath: "id", autoIncrement: true, unique: true });
            };

            webappdb.onsuccess = function(event) {
                let db = event.target.result;
                window.db = db;
            };
            
            webappdb.onerror = function(event) {
                console.log("Erro ao abrir o banco de dados:", event.target.error);
            };

        },
        
        salvar_dados: function(click, data) {
            let db = window.db;

            if (!db) {
                console.log("Banco de dados não inicializado corretamente.");
                return;
            }
            
            let transaction = db.transaction(["dados"], "readwrite");
            let objectStore = transaction.objectStore("dados");
            let webappdb = objectStore.add({dados:data});
            
            webappdb.onsuccess = function(event) {
                console.log("Dados salvos com sucesso!");
            };
            
            webappdb.onerror = function(event) {
                console.log("Erro ao salvar os dados:", event.target.error);
            };
        },
        
        obter_dados: function() {
            let db = window.db;
            
            if (!db) {
                console.log("Banco de dados não inicializado corretamente.");
                return;
            }
            
            let transaction = db.transaction(["dados"], "readonly");
            let objectStore = transaction.objectStore("dados");
            let webappdb = objectStore.getAll();
            
            webappdb.onsuccess = function(event) {
                let data = event.target.result;
                console.log("Dados obtidos:", data);
                window.data = (data);
            };
            
            webappdb.onerror = function(event) {
                console.log("Erro ao obter os dados:", event.target.error);
            };

            return window.data;
        }
    }
});

window.dash_clientside.clientside.iniciar_indexeddb();
