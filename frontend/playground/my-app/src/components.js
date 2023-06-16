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

// For Book list Project

function BookList() {
  return (
    <section className="booklist">
      <Book />
      <Book />
      <Book />
    </section>
  );
}

function Book() {
  return (
    <article className="book">
      <Image />
      <Title />
      <Author />
    </article>
  );
}

const Image = () => (
  <img
    src="https://m.media-amazon.com/images/I/915rw9sjivL._AC_UY218_.jpg"
    alt="Der Eisbär und die Hoffnung auf morgen: Roman"
  />
);
const Title = () => <h2>Der Eisbär und die Hoffnung auf morgen: Roman</h2>;
const Author = () => <h2> John Ironmonger </h2>;

export { BookList, Book };
