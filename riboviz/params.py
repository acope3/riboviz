"""
Workflow configuration parameter names.
"""

INPUT_DIR = "dir_in"
""" Input directory. """
INDEX_DIR = "dir_index"
""" Index files directory. """
TMP_DIR = "dir_tmp"
""" Intermediate files directory. """
OUTPUT_DIR = "dir_out"
""" Output files directory. """

CMD_FILE = "cmd_file"
""" Bash commands file name. """
LOGS_DIR = "dir_logs"
""" Log files directory. """

ORF_FASTA_FILE = "orf_fasta_file"
""" ORF file to align to. """
ORF_GFF_FILE = "orf_gff_file"
""" GFF2/GFF3 file for ORFs. """
RRNA_FASTA_FILE = "rrna_fasta_file"
""" rRNA file to avoid aligning to. """
CODON_POSITIONS_FILE = "codon_positions_file"
""" Codon positions in each gene. """
FEATURES_FILE = "features_file"
""" Features to correlate with ORFs. """
T_RNA_FILE = "t_rna_file"
""" tRNA estimates. """
ASITE_DISP_LENGTH_FILE = "asite_disp_length_file"
""" Fixed A-site positions by read length. """

FQ_FILES = "fq_files"
" fastq files to be processed. """
MULTIPLEX_FQ_FILES = "multiplex_fq_files"
" Multiplexed fastq files to be processed. """

SAMPLE_SHEET = "sample_sheet"
""" Sample sheet. """
DEDUP_UMIS = "dedup_umis"
""" Extract UMIs and deduplicate reads? """
GROUP_UMIS = "group_umis"
""" Summarise UMI groups before and after deduplication? """
DEDUP_STATS = "dedup_stats"
""" Output UMI deduplication statistics? """
EXTRACT_UMIS = "extract_umis"
""" Extract UMIs? """
UMI_REGEXP = "umi_regexp"
"""
UMI-tools-compliant regular expression to extract UMIs and
barcodes.
"""

BUILD_INDICES = "build_indices"
""" Build indices for aligner flag. """
ORF_INDEX_PREFIX = "orf_index_prefix"
""" rRNA index file name prefix. """
RRNA_INDEX_PREFIX = "rrna_index_prefix"
""" ORF index file name prefix. """

ADAPTERS = "adapters"
""" Illumina sequencing adapter to remove. """
MAKE_BEDGRAPH = "make_bedgraph"
""" Output bedgraph files. """
BUFFER = "buffer"
""" Length of flanking region around the CDS. """
COUNT_THRESHOLD = "count_threshold"
"""
Remove genes with a read count below this threshold, when generating
statistics and figures.
"""
DATASET = "dataset"
""" Dataset name. """
DO_POS_SP_NT_FREQ = "do_pos_sp_nt_freq"
""" Calculate position-specific nucleotide frequency? """
MIN_READ_LENGTH = "min_read_length"
""" Minimum read length in H5 output. """
MAX_READ_LENGTH = "max_read_length"
""" Maximum read length in H5 output. """
PRIMARY_ID = "primary_id"
""" Primary gene IDs. """
SECONDARY_ID = "secondary_id"
""" Secondary gene IDs. """
IS_RIBOVIZ_GFF = "is_riboviz_gff"
"""
Does the GFF file contain 3 elements per gene - UTR5, CDS, and UTR3?
"""
RPF = "rpf"
""" Is the dataset an RPF or mRNA dataset? """
STOP_IN_CDS = "stop_in_cds"
""" Are stop codons part of the CDS annotations in GFF? """
COUNT_READS = "count_reads"
"""
Scan input, temporary and output files and produce counts of reads in
each FASTQ, SAM and BAM file processed?
"""

NUM_PROCESSES = "num_processes"
""" Number of processes to parallelize over. """
IS_TEST_RUN = "is_test_run"
""" Is this a test run? (unused). """
ALIGNER = "aligner"
""" Short read aligner to use (unused). """

VALIDATE_ONLY = "validate_only"
""" Validate configuration only? (Nextflow workflow only). """
SKIP_INPUTS = "skip_inputs"
"""
When validating configuration skip checks for existence of ribosome
profiling data files.
"""
