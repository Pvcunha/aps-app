import {
    BrowserRouter as Router,
    Routes,
    Route
} from "react-router-dom"

import { Home } from "./paginas/telaHome";
import { TelaCadastro } from "./paginas/telaCadastro";
import { TelaLogin } from "./paginas/telaLogin";
import { TelaProdutos } from "./paginas/telaProdutos";
import { TelaPagamento } from "./paginas/telaPagamento";

export function AppRoutes() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/cadastro" element={ <TelaCadastro /> } />
                <Route path="/login" element={ <TelaLogin /> }/>
                <Route path="/produtos" element={ <TelaProdutos /> } />
                <Route path="/finalizar" element={ <TelaPagamento /> } />
            </Routes>
        </Router>
    )
}