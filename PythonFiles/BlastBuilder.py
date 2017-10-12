from PythonFiles.Blast import Blast


class BlastBuilder(object):

    def set_WGS_paths(self, path_list: list):
        self.WGS_paths = path_list

    def set_WGS_flags(self, seq_type: str):
        if seq_type is "N":
            self.WGS_flags = "nucl"
        else:
            self.WGS_flags = "prot"

    def set_query_paths(self, path_list: list):
        self.query_paths = path_list

    def set_query_flags(self, seq_type: str):
        if seq_type is "N":
            self.query_flags = "nucl"
        else:
            self.query_flags = "prot"

    def set_blast_param(self, parameter_dict: dict):
        self.blast_parameters = parameter_dict

    def set_output_file(self, target_output: str):
        self.output_path = target_output

    def run_blast(self):
        Blast.make_blast_db(self.WGS_paths, self.WGS_flags)
        Blast.blast_query(self.WGS_paths, self.query_paths, self.output_path, self.blast_parameters)
