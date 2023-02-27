import {
    BrowserRouter as Router,
    Routes,
    Route
} from "react-router-dom"

import { Home } from "./paginas/telaHome"
import { TelaCadastro } from "./paginas/telaCadastro"
import { TelaLogin } from "./paginas/telaLogin"
export function AppRoutes() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/cadastro" element={ <TelaCadastro /> } />
                <Route path="/login" element={ <TelaLogin /> }/>
            </Routes>
        </Router>
    )
}