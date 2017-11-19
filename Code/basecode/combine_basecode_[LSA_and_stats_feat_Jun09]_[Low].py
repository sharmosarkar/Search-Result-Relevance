
"""
    This file generates one combination of feature set (Low).

"""

import sys
sys.path.append("../")
from param_config import config
from gen_info import gen_info
from combine_basecode import combine_feat, SimpleTransform

            
if __name__ == "__main__":

    feat_names = [

        ##############
        ## Query id ##
        ##############
        ("qid", SimpleTransform()),

        ################
        ## Word count ##
        ################
        ('count_of_query_unigram', SimpleTransform(config.count_feat_transform)),
        ('count_of_unique_query_unigram', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_unique_query_unigram', SimpleTransform()),
        ('count_of_query_bigram', SimpleTransform(config.count_feat_transform)),
        ('count_of_unique_query_bigram', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_unique_query_bigram', SimpleTransform()),
        ('count_of_query_trigram', SimpleTransform(config.count_feat_transform)),
        ('count_of_unique_query_trigram', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_unique_query_trigram', SimpleTransform()),
        ('count_of_digit_in_query', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_digit_in_query', SimpleTransform()),
        ('count_of_title_unigram', SimpleTransform(config.count_feat_transform)),
        ('count_of_unique_title_unigram', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_unique_title_unigram', SimpleTransform()),
        ('count_of_title_bigram', SimpleTransform(config.count_feat_transform)),
        ('count_of_unique_title_bigram', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_unique_title_bigram', SimpleTransform()),
        ('count_of_title_trigram', SimpleTransform(config.count_feat_transform)),
        ('count_of_unique_title_trigram', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_unique_title_trigram', SimpleTransform()),
        ('count_of_digit_in_title', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_digit_in_title', SimpleTransform()),
        ('count_of_description_unigram', SimpleTransform(config.count_feat_transform)),
        ('count_of_unique_description_unigram', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_unique_description_unigram', SimpleTransform()),
        ('count_of_description_bigram', SimpleTransform(config.count_feat_transform)),
        ('count_of_unique_description_bigram', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_unique_description_bigram', SimpleTransform()),
        ('count_of_description_trigram', SimpleTransform(config.count_feat_transform)),
        ('count_of_unique_description_trigram', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_unique_description_trigram', SimpleTransform()),
        ('count_of_digit_in_description', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_digit_in_description', SimpleTransform()),
        ('count_of_query_unigram_in_title', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_query_unigram_in_title', SimpleTransform()),
        ('count_of_query_unigram_in_description', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_query_unigram_in_description', SimpleTransform()),
        ('count_of_title_unigram_in_query', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_title_unigram_in_query', SimpleTransform()),
        ('count_of_title_unigram_in_description', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_title_unigram_in_description', SimpleTransform()),
        ('count_of_description_unigram_in_query', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_description_unigram_in_query', SimpleTransform()),
        ('count_of_description_unigram_in_title', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_description_unigram_in_title', SimpleTransform()),
        ('title_unigram_in_query_div_query_unigram', SimpleTransform()),
        ('title_unigram_in_query_div_query_unigram_in_title', SimpleTransform()),
        ('description_unigram_in_query_div_query_unigram', SimpleTransform()),
        ('description_unigram_in_query_div_query_unigram_in_description', SimpleTransform()),
        ('count_of_query_bigram_in_title', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_query_bigram_in_title', SimpleTransform()),
        ('count_of_query_bigram_in_description', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_query_bigram_in_description', SimpleTransform()),
        ('count_of_title_bigram_in_query', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_title_bigram_in_query', SimpleTransform()),
        ('count_of_title_bigram_in_description', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_title_bigram_in_description', SimpleTransform()),
        ('count_of_description_bigram_in_query', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_description_bigram_in_query', SimpleTransform()),
        ('count_of_description_bigram_in_title', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_description_bigram_in_title', SimpleTransform()),
        ('title_bigram_in_query_div_query_bigram', SimpleTransform()),
        ('title_bigram_in_query_div_query_bigram_in_title', SimpleTransform()),
        ('description_bigram_in_query_div_query_bigram', SimpleTransform()),
        ('description_bigram_in_query_div_query_bigram_in_description', SimpleTransform()),
        ('count_of_query_trigram_in_title', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_query_trigram_in_title', SimpleTransform()),
        ('count_of_query_trigram_in_description', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_query_trigram_in_description', SimpleTransform()),
        ('count_of_title_trigram_in_query', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_title_trigram_in_query', SimpleTransform()),
        ('count_of_title_trigram_in_description', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_title_trigram_in_description', SimpleTransform()),
        ('count_of_description_trigram_in_query', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_description_trigram_in_query', SimpleTransform()),
        ('count_of_description_trigram_in_title', SimpleTransform(config.count_feat_transform)),
        ('ratio_of_description_trigram_in_title', SimpleTransform()),
        ('title_trigram_in_query_div_query_trigram', SimpleTransform()),
        ('title_trigram_in_query_div_query_trigram_in_title', SimpleTransform()),
        ('description_trigram_in_query_div_query_trigram', SimpleTransform()),
        ('description_trigram_in_query_div_query_trigram_in_description', SimpleTransform()),

        ##############
        ## Position ##
        ##############
        ('pos_of_title_unigram_in_query_min', SimpleTransform(config.count_feat_transform)),
        ('pos_of_title_unigram_in_query_mean', SimpleTransform(config.count_feat_transform)),
        ('pos_of_title_unigram_in_query_median', SimpleTransform(config.count_feat_transform)),
        ('pos_of_title_unigram_in_query_max', SimpleTransform(config.count_feat_transform)),
        ('pos_of_title_unigram_in_query_std', SimpleTransform(config.count_feat_transform)),
        ('normalized_pos_of_title_unigram_in_query_min', SimpleTransform()),
        ('normalized_pos_of_title_unigram_in_query_mean', SimpleTransform()),
        ('normalized_pos_of_title_unigram_in_query_median', SimpleTransform()),
        ('normalized_pos_of_title_unigram_in_query_max', SimpleTransform()),
        ('normalized_pos_of_title_unigram_in_query_std', SimpleTransform()),
        ('pos_of_description_unigram_in_query_min', SimpleTransform(config.count_feat_transform)),
        ('pos_of_description_unigram_in_query_mean', SimpleTransform(config.count_feat_transform)),
        ('pos_of_description_unigram_in_query_median', SimpleTransform(config.count_feat_transform)),
        ('pos_of_description_unigram_in_query_max', SimpleTransform(config.count_feat_transform)),
        ('pos_of_description_unigram_in_query_std', SimpleTransform(config.count_feat_transform)),
        ('normalized_pos_of_description_unigram_in_query_min', SimpleTransform()),
        ('normalized_pos_of_description_unigram_in_query_mean', SimpleTransform()),
        ('normalized_pos_of_description_unigram_in_query_median', SimpleTransform()),
        ('normalized_pos_of_description_unigram_in_query_max', SimpleTransform()),
        ('normalized_pos_of_description_unigram_in_query_std', SimpleTransform()),
        ('pos_of_query_unigram_in_title_min', SimpleTransform(config.count_feat_transform)),
        ('pos_of_query_unigram_in_title_mean', SimpleTransform(config.count_feat_transform)),
        ('pos_of_query_unigram_in_title_median', SimpleTransform(config.count_feat_transform)),
        ('pos_of_query_unigram_in_title_max', SimpleTransform(config.count_feat_transform)),
        ('pos_of_query_unigram_in_title_std', SimpleTransform(config.count_feat_transform)),
        ('normalized_pos_of_query_unigram_in_title_min', SimpleTransform()),
        ('normalized_pos_of_query_unigram_in_title_mean', SimpleTransform()),
        ('normalized_pos_of_query_unigram_in_title_median', SimpleTransform()),
        ('normalized_pos_of_query_unigram_in_title_max', SimpleTransform()),
        ('normalized_pos_of_query_unigram_in_title_std', SimpleTransform()),
        ('pos_of_description_unigram_in_title_min', SimpleTransform(config.count_feat_transform)),
        ('pos_of_description_unigram_in_title_mean', SimpleTransform(config.count_feat_transform)),
        ('pos_of_description_unigram_in_title_median', SimpleTransform(config.count_feat_transform)),
        ('pos_of_description_unigram_in_title_max', SimpleTransform(config.count_feat_transform)),
        ('pos_of_description_unigram_in_title_std', SimpleTransform(config.count_feat_transform)),
        ('normalized_pos_of_description_unigram_in_title_min', SimpleTransform()),
        ('normalized_pos_of_description_unigram_in_title_mean', SimpleTransform()),
        ('normalized_pos_of_description_unigram_in_title_median', SimpleTransform()),
        ('normalized_pos_of_description_unigram_in_title_max', SimpleTransform()),
        ('normalized_pos_of_description_unigram_in_title_std', SimpleTransform()),
        ('pos_of_query_unigram_in_description_min', SimpleTransform(config.count_feat_transform)),
        ('pos_of_query_unigram_in_description_mean', SimpleTransform(config.count_feat_transform)),
        ('pos_of_query_unigram_in_description_median', SimpleTransform(config.count_feat_transform)),
        ('pos_of_query_unigram_in_description_max', SimpleTransform(config.count_feat_transform)),
        ('pos_of_query_unigram_in_description_std', SimpleTransform(config.count_feat_transform)),
        ('normalized_pos_of_query_unigram_in_description_min', SimpleTransform()),
        ('normalized_pos_of_query_unigram_in_description_mean', SimpleTransform()),
        ('normalized_pos_of_query_unigram_in_description_median', SimpleTransform()),
        ('normalized_pos_of_query_unigram_in_description_max', SimpleTransform()),
        ('normalized_pos_of_query_unigram_in_description_std', SimpleTransform()),
        ('pos_of_title_unigram_in_description_min', SimpleTransform(config.count_feat_transform)),
        ('pos_of_title_unigram_in_description_mean', SimpleTransform(config.count_feat_transform)),
        ('pos_of_title_unigram_in_description_median', SimpleTransform(config.count_feat_transform)),
        ('pos_of_title_unigram_in_description_max', SimpleTransform(config.count_feat_transform)),
        ('pos_of_title_unigram_in_description_std', SimpleTransform(config.count_feat_transform)),
        ('normalized_pos_of_title_unigram_in_description_min', SimpleTransform()),
        ('normalized_pos_of_title_unigram_in_description_mean', SimpleTransform()),
        ('normalized_pos_of_title_unigram_in_description_median', SimpleTransform()),
        ('normalized_pos_of_title_unigram_in_description_max', SimpleTransform()),
        ('normalized_pos_of_title_unigram_in_description_std', SimpleTransform()),
        # ('pos_of_title_bigram_in_query_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_bigram_in_query_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_bigram_in_query_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_bigram_in_query_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_bigram_in_query_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_title_bigram_in_query_min', SimpleTransform()),
        # ('normalized_pos_of_title_bigram_in_query_mean', SimpleTransform()),
        # ('normalized_pos_of_title_bigram_in_query_median', SimpleTransform()),
        # ('normalized_pos_of_title_bigram_in_query_max', SimpleTransform()),
        # ('normalized_pos_of_title_bigram_in_query_std', SimpleTransform()),
        # ('pos_of_description_bigram_in_query_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_bigram_in_query_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_bigram_in_query_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_bigram_in_query_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_bigram_in_query_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_description_bigram_in_query_min', SimpleTransform()),
        # ('normalized_pos_of_description_bigram_in_query_mean', SimpleTransform()),
        # ('normalized_pos_of_description_bigram_in_query_median', SimpleTransform()),
        # ('normalized_pos_of_description_bigram_in_query_max', SimpleTransform()),
        # ('normalized_pos_of_description_bigram_in_query_std', SimpleTransform()),
        # ('pos_of_query_bigram_in_title_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_bigram_in_title_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_bigram_in_title_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_bigram_in_title_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_bigram_in_title_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_query_bigram_in_title_min', SimpleTransform()),
        # ('normalized_pos_of_query_bigram_in_title_mean', SimpleTransform()),
        # ('normalized_pos_of_query_bigram_in_title_median', SimpleTransform()),
        # ('normalized_pos_of_query_bigram_in_title_max', SimpleTransform()),
        # ('normalized_pos_of_query_bigram_in_title_std', SimpleTransform()),
        # ('pos_of_description_bigram_in_title_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_bigram_in_title_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_bigram_in_title_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_bigram_in_title_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_bigram_in_title_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_description_bigram_in_title_min', SimpleTransform()),
        # ('normalized_pos_of_description_bigram_in_title_mean', SimpleTransform()),
        # ('normalized_pos_of_description_bigram_in_title_median', SimpleTransform()),
        # ('normalized_pos_of_description_bigram_in_title_max', SimpleTransform()),
        # ('normalized_pos_of_description_bigram_in_title_std', SimpleTransform()),
        # ('pos_of_query_bigram_in_description_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_bigram_in_description_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_bigram_in_description_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_bigram_in_description_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_bigram_in_description_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_query_bigram_in_description_min', SimpleTransform()),
        # ('normalized_pos_of_query_bigram_in_description_mean', SimpleTransform()),
        # ('normalized_pos_of_query_bigram_in_description_median', SimpleTransform()),
        # ('normalized_pos_of_query_bigram_in_description_max', SimpleTransform()),
        # ('normalized_pos_of_query_bigram_in_description_std', SimpleTransform()),
        # ('pos_of_title_bigram_in_description_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_bigram_in_description_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_bigram_in_description_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_bigram_in_description_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_bigram_in_description_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_title_bigram_in_description_min', SimpleTransform()),
        # ('normalized_pos_of_title_bigram_in_description_mean', SimpleTransform()),
        # ('normalized_pos_of_title_bigram_in_description_median', SimpleTransform()),
        # ('normalized_pos_of_title_bigram_in_description_max', SimpleTransform()),
        # ('normalized_pos_of_title_bigram_in_description_std', SimpleTransform()),
        # ('pos_of_title_trigram_in_query_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_trigram_in_query_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_trigram_in_query_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_trigram_in_query_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_trigram_in_query_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_title_trigram_in_query_min', SimpleTransform()),
        # ('normalized_pos_of_title_trigram_in_query_mean', SimpleTransform()),
        # ('normalized_pos_of_title_trigram_in_query_median', SimpleTransform()),
        # ('normalized_pos_of_title_trigram_in_query_max', SimpleTransform()),
        # ('normalized_pos_of_title_trigram_in_query_std', SimpleTransform()),
        # ('pos_of_description_trigram_in_query_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_trigram_in_query_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_trigram_in_query_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_trigram_in_query_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_trigram_in_query_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_description_trigram_in_query_min', SimpleTransform()),
        # ('normalized_pos_of_description_trigram_in_query_mean', SimpleTransform()),
        # ('normalized_pos_of_description_trigram_in_query_median', SimpleTransform()),
        # ('normalized_pos_of_description_trigram_in_query_max', SimpleTransform()),
        # ('normalized_pos_of_description_trigram_in_query_std', SimpleTransform()),
        # ('pos_of_query_trigram_in_title_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_trigram_in_title_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_trigram_in_title_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_trigram_in_title_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_trigram_in_title_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_query_trigram_in_title_min', SimpleTransform()),
        # ('normalized_pos_of_query_trigram_in_title_mean', SimpleTransform()),
        # ('normalized_pos_of_query_trigram_in_title_median', SimpleTransform()),
        # ('normalized_pos_of_query_trigram_in_title_max', SimpleTransform()),
        # ('normalized_pos_of_query_trigram_in_title_std', SimpleTransform()),
        # ('pos_of_description_trigram_in_title_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_trigram_in_title_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_trigram_in_title_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_trigram_in_title_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_description_trigram_in_title_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_description_trigram_in_title_min', SimpleTransform()),
        # ('normalized_pos_of_description_trigram_in_title_mean', SimpleTransform()),
        # ('normalized_pos_of_description_trigram_in_title_median', SimpleTransform()),
        # ('normalized_pos_of_description_trigram_in_title_max', SimpleTransform()),
        # ('normalized_pos_of_description_trigram_in_title_std', SimpleTransform()),
        # ('pos_of_query_trigram_in_description_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_trigram_in_description_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_trigram_in_description_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_trigram_in_description_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_query_trigram_in_description_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_query_trigram_in_description_min', SimpleTransform()),
        # ('normalized_pos_of_query_trigram_in_description_mean', SimpleTransform()),
        # ('normalized_pos_of_query_trigram_in_description_median', SimpleTransform()),
        # ('normalized_pos_of_query_trigram_in_description_max', SimpleTransform()),
        # ('normalized_pos_of_query_trigram_in_description_std', SimpleTransform()),
        # ('pos_of_title_trigram_in_description_min', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_trigram_in_description_mean', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_trigram_in_description_median', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_trigram_in_description_max', SimpleTransform(config.count_feat_transform)),
        # ('pos_of_title_trigram_in_description_std', SimpleTransform(config.count_feat_transform)),
        # ('normalized_pos_of_title_trigram_in_description_min', SimpleTransform()),
        # ('normalized_pos_of_title_trigram_in_description_mean', SimpleTransform()),
        # ('normalized_pos_of_title_trigram_in_description_median', SimpleTransform()),
        # ('normalized_pos_of_title_trigram_in_description_max', SimpleTransform()),
        # ('normalized_pos_of_title_trigram_in_description_std', SimpleTransform()),

        ('description_missing', SimpleTransform()),

        ## jaccard coef
        ('jaccard_coef_of_unigram_between_query_title', SimpleTransform()),
        ('jaccard_coef_of_unigram_between_query_description', SimpleTransform()),
        ('jaccard_coef_of_unigram_between_title_description', SimpleTransform()),
        ('jaccard_coef_of_bigram_between_query_title', SimpleTransform()),
        ('jaccard_coef_of_bigram_between_query_description', SimpleTransform()),
        ('jaccard_coef_of_bigram_between_title_description', SimpleTransform()),
        ('jaccard_coef_of_trigram_between_query_title', SimpleTransform()),
        ('jaccard_coef_of_trigram_between_query_description', SimpleTransform()),
        ('jaccard_coef_of_trigram_between_title_description', SimpleTransform()),

        ## dice dist
        ('dice_dist_of_unigram_between_query_title', SimpleTransform()),
        ('dice_dist_of_unigram_between_query_description', SimpleTransform()),
        ('dice_dist_of_unigram_between_title_description', SimpleTransform()),
        ('dice_dist_of_bigram_between_query_title', SimpleTransform()),
        ('dice_dist_of_bigram_between_query_description', SimpleTransform()),
        ('dice_dist_of_bigram_between_title_description', SimpleTransform()),
        ('dice_dist_of_trigram_between_query_title', SimpleTransform()),
        ('dice_dist_of_trigram_between_query_description', SimpleTransform()),
        ('dice_dist_of_trigram_between_title_description', SimpleTransform()),

        # ## jaccard coef stats feat
        # ("title_unigram_jaccard_coef_stats_feat_by_relevance", SimpleTransform()),
        # ("title_unigram_jaccard_coef_stats_feat_by_query_relevance", SimpleTransform()),
        # ("title_bigram_jaccard_coef_stats_feat_by_relevance", SimpleTransform()),
        # ("title_bigram_jaccard_coef_stats_feat_by_query_relevance", SimpleTransform()),
        # ("title_trigram_jaccard_coef_stats_feat_by_relevance", SimpleTransform()),
        # ("title_trigram_jaccard_coef_stats_feat_by_query_relevance", SimpleTransform()),
        # ("description_unigram_jaccard_coef_stats_feat_by_relevance", SimpleTransform()),
        # ("description_unigram_jaccard_coef_stats_feat_by_query_relevance", SimpleTransform()),
        # ("description_bigram_jaccard_coef_stats_feat_by_relevance", SimpleTransform()),
        # ("description_bigram_jaccard_coef_stats_feat_by_query_relevance", SimpleTransform()),
        # ("description_trigram_jaccard_coef_stats_feat_by_relevance", SimpleTransform()),
        # ("description_trigram_jaccard_coef_stats_feat_by_query_relevance", SimpleTransform()),

        #  ## dice dist stats feat
        # ("title_unigram_dice_dist_stats_feat_by_relevance", SimpleTransform()),
        # ("title_unigram_dice_dist_stats_feat_by_query_relevance", SimpleTransform()),
        # ("title_bigram_dice_dist_stats_feat_by_relevance", SimpleTransform()),
        # ("title_bigram_dice_dist_stats_feat_by_query_relevance", SimpleTransform()),
        # ("title_trigram_dice_dist_stats_feat_by_relevance", SimpleTransform()),
        # ("title_trigram_dice_dist_stats_feat_by_query_relevance", SimpleTransform()),
        # ("description_unigram_dice_dist_stats_feat_by_relevance", SimpleTransform()),
        # ("description_unigram_dice_dist_stats_feat_by_query_relevance", SimpleTransform()),
        # ("description_bigram_dice_dist_stats_feat_by_relevance", SimpleTransform()),
        # ("description_bigram_dice_dist_stats_feat_by_query_relevance", SimpleTransform()),
        # ("description_trigram_dice_dist_stats_feat_by_relevance", SimpleTransform()),
        # ("description_trigram_dice_dist_stats_feat_by_query_relevance", SimpleTransform()),
        
        ############
        ## TF-IDF ##
        ############
        # ('query_tfidf_common_vocabulary', SimpleTransform()),
        # ('title_tfidf_common_vocabulary', SimpleTransform()),
        # ('description_tfidf_common_vocabulary', SimpleTransform()),
        ('title_tfidf_common_vocabulary_cosine_sim_stats_feat_by_relevance', SimpleTransform()),
        ('title_tfidf_common_vocabulary_cosine_sim_stats_feat_by_query_relevance', SimpleTransform()),
        ('description_tfidf_common_vocabulary_cosine_sim_stats_feat_by_relevance', SimpleTransform()),
        ('description_tfidf_common_vocabulary_cosine_sim_stats_feat_by_query_relevance', SimpleTransform()),
        ('query_tfidf_common_vocabulary_title_tfidf_common_vocabulary_tfidf_cosine_sim', SimpleTransform()),
        ('query_tfidf_common_vocabulary_description_tfidf_common_vocabulary_tfidf_cosine_sim', SimpleTransform()),
        ('title_tfidf_common_vocabulary_description_tfidf_common_vocabulary_tfidf_cosine_sim', SimpleTransform()),
        # ('query_tfidf_common_vocabulary_common_svd100', SimpleTransform()),
        # ('title_tfidf_common_vocabulary_common_svd100', SimpleTransform()),
        # ('title_tfidf_common_vocabulary_common_svd100_cosine_sim_stats_feat_by_relevance', SimpleTransform()),
        # ('title_tfidf_common_vocabulary_common_svd100_cosine_sim_stats_feat_by_query_relevance', SimpleTransform()),
        # ('description_tfidf_common_vocabulary_common_svd100', SimpleTransform()),
        # ('description_tfidf_common_vocabulary_common_svd100_cosine_sim_stats_feat_by_relevance', SimpleTransform()),
        # ('description_tfidf_common_vocabulary_common_svd100_cosine_sim_stats_feat_by_query_relevance', SimpleTransform()),
        # ('query_tfidf_common_vocabulary_title_tfidf_common_vocabulary_tfidf_common_svd100_cosine_sim', SimpleTransform()),
        # ('query_tfidf_common_vocabulary_description_tfidf_common_vocabulary_tfidf_common_svd100_cosine_sim', SimpleTransform()),
        # ('title_tfidf_common_vocabulary_description_tfidf_common_vocabulary_tfidf_common_svd100_cosine_sim', SimpleTransform()),
        ('query_tfidf_common_vocabulary_individual_svd100', SimpleTransform()),
        ('title_tfidf_common_vocabulary_individual_svd100', SimpleTransform()),
        # ('title_tfidf_common_vocabulary_individual_svd100_cosine_sim_stats_feat_by_relevance', SimpleTransform()),
        # ('title_tfidf_common_vocabulary_individual_svd100_cosine_sim_stats_feat_by_query_relevance', SimpleTransform()),
        ('description_tfidf_common_vocabulary_individual_svd100', SimpleTransform()),
        # ('description_tfidf_common_vocabulary_individual_svd100_cosine_sim_stats_feat_by_relevance', SimpleTransform()),
        # ('description_tfidf_common_vocabulary_individual_svd100_cosine_sim_stats_feat_by_query_relevance', SimpleTransform()),

    ]

    gen_info(feat_path_name="LSA_and_stats_feat_Jun09")
    combine_feat(feat_names, feat_path_name="LSA_and_stats_feat_Jun09")