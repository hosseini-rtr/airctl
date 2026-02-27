import os
from abc import ABC, abstractmethod
from platform import system

OS_TYPE = system()

print(f"OS_TYPE: {OS_TYPE}")


class WorkspaceSwiper(ABC):
    @abstractmethod
    def swipe(self):
        pass


class MacWorkSpaceSwiper(WorkspaceSwiper):
    def swipe(self):
        # ACTION_TAG: Swipe left
        os.system(
            "osascript -e 'tell application \"System Events\" to key code 123 using control down'"
        )
        # ACTION_TAG: Swipe right
        os.system(
            "osascript -e 'tell application \"System Events\" to key code 124 using control down'"
        )


def swipe_work_space():
    if OS_TYPE == "Darwin":  # macOS
        swiper = MacWorkSpaceSwiper()
        return swiper.swipe()

    elif OS_TYPE == "Windows":
        os.system(
            'powershell -command "(New-Object -ComObject Shell.Application).MinimizeAll()"'
        )  # Minimize all windows
        os.system(
            'powershell -command "(New-Object -ComObject Shell.Application).UndoMinimizeAll()"'
        )  # Restore all windows
    else:
        print("Unsupported OS. Swipe workspace functionality is not available.")


if __name__ == "__main__":
    swipe_work_space()
