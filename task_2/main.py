from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string.")
        if pattern == "":
            raise ValueError("Pattern cannot be empty.")
        count = 0

        stack = [(self.root, "")]

        while stack:
            current_node, current_word = stack.pop()
            if (current_node.value is not None
                and current_word.endswith(pattern)):
                count += 1
            for character, child_node in current_node.children.items():
                new_word = current_word + character
                stack.append((child_node, new_word))
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")
        
        if prefix == "":
            raise ValueError("Prefix cannot be empty")
        current_node = self.root
        for character in prefix:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return True
               

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat