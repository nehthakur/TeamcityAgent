import zipfile
import tempfile


def extract_project(uploaded_file):

    all_content = ""

    with tempfile.TemporaryDirectory() as temp_dir:

        with zipfile.ZipFile(uploaded_file) as zip_ref:

            zip_ref.extractall(temp_dir)

            for file_info in zip_ref.infolist():

                if (
                    file_info.filename.endswith(".kt")
                    or
                    file_info.filename.endswith(".kts")
                ):

                    path = f"{temp_dir}/{file_info.filename}"

                    try:

                        with open(
                            path,
                            "r",
                            encoding="utf-8"
                        ) as f:

                            all_content += "\n"
                            all_content += f.read()

                    except Exception:
                        pass

    return all_content
