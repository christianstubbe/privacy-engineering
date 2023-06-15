const Greeting = () => {
  return (
    <div>
      <Person />
      <Message />
    </div>
  );
};

const Person = () => <h3>Ettore Marangon</h3>;
const Message = () => <h2>Hallo World</h2>;

export default { Greeting, Person, Message };
