dict1 = {
        "Python":"Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code.",
        "Javascript":"JavaScript was developed by Brendan Eich in 1995, which appeared in Netscape, a popular browser of that time. The language was initially called LiveScript and was later renamed JavaScript. There are many programmers who think that JavaScript and Java are the same. In fact, JavaScript and Java are very much unrelated.",
        "Java":"Java is a high-level programming language developed by Sun Microsystems. ... Instead, Java programs are interpreted by the Java Virtual Machine, or JVM, which runs on multiple platforms. This means all Java programs are multiplatform and can run on different platforms, including Macintosh, Windows, and Unix computers.",
        "C++":"C++ is a cross-platform language that can be used to create high-performance applications. C++ was developed by Bjarne Stroustrup, as an extension to the C language. C++ gives programmers a high level of control over system resources and memory.",
        "Php":"PHP is a recursive acronym for \"PHP: Hypertext Preprocessor\". PHP is a server side scripting language that is embedded in HTML. It is used to manage dynamic content, databases, session tracking, even build entire e-commerce sites."

}
print("You can search the defination of given below :\n \b\"Python\" , \"JavaScript\" , \"Java\" , \"C++\" , \"Php\"")
print(dict1.keys())
print("Enter the word which you wanna search")
key_input = input()
lower = key_input.lower()
capitalize =  lower.capitalize()
print(dict1.get(capitalize))