#include <iostream>
#include <optional>
#include <format>
#include <string>

std::optional<int> returnInt(int n = 0)
{
    if (n < 1)
        return std::nullopt;
    else
        return n;
}

int main()
{
    auto n{ returnInt() };

    std::string ans{};

    if (n.has_value())
        ans = std::format("The answer is: {}", n.value_or(0));
    else
        ans = "no answer";

    std::cout << ans;

    return EXIT_SUCCESS;
}
