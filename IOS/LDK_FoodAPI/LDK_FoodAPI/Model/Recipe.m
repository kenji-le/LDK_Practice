//
//  Recipe.m
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "Recipe.h"

@implementation Recipe

+ (Recipe *)recipeFromDictionary:(NSDictionary *)recipeDict {
    Recipe *recipe = [[Recipe alloc] init];
    recipe.publisher = [recipeDict objectForKey:KEY_PUBPLISHER];
    recipe.f2fUrl = [recipeDict objectForKey:KEY_F2F_URL];
    recipe.title = [recipeDict objectForKey:KEY_TITLE];
    recipe.sourceUrl = [recipeDict objectForKey:KEY_SOURCE_URL];
    recipe.recipeId = [recipeDict objectForKey:KEY_RECIPE_ID];
    recipe.imageUrl = [recipeDict objectForKey:KEY_IMAGE_URL];
    recipe.socialRank = [recipeDict objectForKey:KEY_SOCIAL_RANK];
    recipe.publisherUrl = [recipeDict objectForKey:KEY_PUBPLISHER_URL];
    
    return recipe;
}

@end
