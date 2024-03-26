from typing import Any, List


class Name:

    def __init__(self):
        self.names_env = []
        self.length = len(self.names_env)

    def __call__(self, name_env: str) -> str:
        self.names_env.append(name_env)
        self.length = len(self.names_env)
        return name_env

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < len(self.names_env):
            x = self.names_env[self.a]
            self.a += 1
            return x
        else:
            raise StopIteration


class EnvironWebSite:
    fild = Name()

    host = fild("HOST_WEB_SITE")
    port = fild("PORT_WEB_SITE")

    resurce_folder = fild("RESURCE_WEB_SITE")

    debug = fild("DEBUG_WEB_SITE")


class EnvironSection:
    website = EnvironWebSite


def __add_env_section(odj: object):

    len_seport = 120

    name = " | " + str(odj().__class__.__name__) + " | "

    hader = "\n".join(
        ("=" * len_seport, f"| {name:-^{len_seport - 4}} |", "=" * len_seport)
    )

    body = "\n".join([f"{i}=exchange" for i in odj.fild])

    end = "=" * len_seport

    print("\n\n".join([hader, body, end]))

    with open(".env", "a+") as f:
        f.write("\n\n".join([hader, body, end]) + "\n\n\n\n")


if __name__ == "__main__":
    __add_env_section(EnvironWebSite)
