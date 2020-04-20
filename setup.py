if platform.system() == "Darwin":
            get_ipython().system(
                u"if [ ! -d '/opt/hopper' ]; then git clone https://github.com/Olliebear/underactuated_final_project.git /opt/hopper fi"  # noqa
            )
        elif platform.linux_distribution() == ("Ubuntu", "18.04", "bionic"):
            get_ipython().system(
                u"if [ ! -d '/opt/hopper' ]; then git clone https://github.com/Olliebear/underactuated_final_project.git /opt/hopper fi"  # noqa
            )
        else:
            assert False, "Unsupported platform"
        sys.path.append("/opt/hopper")
