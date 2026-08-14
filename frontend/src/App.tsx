import Header from "./components/Header";
import Chat from "./components/Chat";

function App() {
  return (
    <main className="app">
      <div className="chat-container">
        <Header />

        <Chat />
      </div>
    </main>
  );
}

export default App;