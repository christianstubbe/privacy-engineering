import book_img from "./images/book_img.jpg";
import book2_img from "./images/book2_img.jpg";

const firstBook = {
  author: "John Ironmonger",
  title: "Der Eisbär und die Hoffnung auf morgen: Roman",
  img: book_img,
};

const secondBook = {
  author: "Dora Heldt ",
  title: "Liebe oder Eierlikör",
  img: book2_img,
};

// For Book list Project
function BookList() {
  return (
    <section className="booklist">
      <Book
        author={firstBook.author}
        title={firstBook.title}
        img={firstBook.img}
      />
      <Book
        author={secondBook.author}
        title={secondBook.title}
        img={secondBook.img}
      />
    </section>
  );
}

// props = properties
function Book(props) {
  console.log(props);
  return (
    <article className="book">
      <img src={props.img} alt={props.title} />
      <h2>{props.title}</h2>
      <h4>{props.author}</h4>
    </article>
  );
}

// const Image = () => (
//   <img src={book_img} alt="Der Eisbär und die Hoffnung auf morgen: Roman" />
// );
// const Title = () => {
//   const title = "Der Eisbär und die Hoffnung auf morgen: Roman";
//   return <h2>{title}</h2>;
// };
// const Author = () => {
//   const author = "John Ironmonger";
//   // OBJECT Variable to pass style settings
//   const inlineHeadingStyle = {
//     color: "#617d98",
//     fontSize: "0.75rem",
//     marginTop: "0.5rem",
//     letterSpacing: "2px",
//   };
//   // pass JS Object in style
//   return <h4 style={inlineHeadingStyle}> {author}</h4>;
// };

export { BookList, Book };
